package com.learn.easyboot.json;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonRootName;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.databind.SerializerProvider;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.StdSerializer;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.validation.constraints.NotNull;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws JsonProcessingException, ParseException {
        ExtendableBean bean = ExtendableBean.builder()
                .name("My bean name")
                .properties(new HashMap<>())
                .build();
        bean.add("attr1", "val1");
        bean.add("attr2", "val2");

        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.WRAP_ROOT_VALUE);
        String result = mapper.writeValueAsString(bean);
        System.out.println(result);

        System.out.println(new ObjectMapper()
                .writeValueAsString(TypeEnumWithValue.TYPE1));


        SimpleDateFormat df
                = new SimpleDateFormat("dd-MM-yyyy hh:mm:ss");

        String toParse = "20-12-2014 02:30:00";
        Date date = df.parse(toParse);
        EventWithSerializer event = new EventWithSerializer("party", date);

        System.out.println(new ObjectMapper().writeValueAsString(event));


        String json = "{\"id\":1,\"theName\":\"My bean\"}";

        BeanWithCreator bean2 = new ObjectMapper()
                .readerFor(BeanWithCreator.class)
                .readValue(json);
        System.out.println(bean2);

    }
}

@NoArgsConstructor
@AllArgsConstructor
@Builder
@JsonPropertyOrder({ "properties", "name" })
@JsonRootName(value = "bean")
class ExtendableBean {
    @NotNull
    public String name;
    private Map<String, String> properties;
    public String json;

    @JsonAnyGetter
    public Map<String, String> getProperties() {
        return properties;
    }

    public void add(String attr1, String val1) {
        properties.put(attr1, val1);
    }
}

enum TypeEnumWithValue {
    TYPE1(1, "Type A"), TYPE2(2, "Type 2");

    @JsonValue
    private Integer id;
    private String name;

    TypeEnumWithValue(int i, String s) {
        this.id = i;
        this.name = s;
    }

    // standard constructors

//    @JsonValue
//    public String getName() {
//        return name;
//    }
}

@AllArgsConstructor
class EventWithSerializer {
    public String name;

    @JsonSerialize(using = CustomDateSerializer.class)
    public Date eventDate;
}

class CustomDateSerializer extends StdSerializer<Date> {

    private static SimpleDateFormat formatter
            = new SimpleDateFormat("dd-MM-yyyy hh:mm:ss");

    public CustomDateSerializer() {
        this(null);
    }

    public CustomDateSerializer(Class<Date> t) {
        super(t);
    }

    @Override
    public void serialize(Date date, JsonGenerator jsonGenerator, SerializerProvider serializerProvider) throws IOException {
        jsonGenerator.writeString(formatter.format(date) + "done");
    }
//
//    @Override
//    public void serialize(
//            Date value, JsonGenerator gen, SerializerProvider arg2)
//            throws IOException, JsonProcessingException {
//        gen.writeString(formatter.format(value));
//    }
}

@Getter
@Setter
@NoArgsConstructor
class BeanWithCreator {
    public int id;
    public String name;

    @JsonCreator
    public BeanWithCreator(
            @JsonProperty("id") int id,
            @JsonProperty("theName") String name) {
        this.id = id;
        this.name = name;
    }
}

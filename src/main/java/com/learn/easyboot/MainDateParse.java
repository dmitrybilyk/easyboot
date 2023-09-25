package com.learn.easyboot;

import java.time.LocalDateTime;
import java.time.OffsetDateTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeFormatterBuilder;

public class MainDateParse {
    public static void main(String[] args) {
        String source = "2017-10-12 16:54:26.737+03";
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter
                .ofPattern("yyyy-MM-dd HH:mm:ss.nnn VV");
        OffsetDateTime localDateTime = OffsetDateTime.parse(source, DateTimeFormatter.BASIC_ISO_DATE);
    }
}

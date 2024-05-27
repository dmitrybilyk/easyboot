public class generate {
    public static void main(String[] args) {
        String s = "";
        for(int i=0; i<1000;i++){
            s += ",\"callrec:voicetagid:"+i + "\"";
        }
        System.out.println(s);
    }
}

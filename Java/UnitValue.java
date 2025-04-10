class UnitValue {
    private String display;
    private String category;
    private double factor;
    private double offset;
    private double value;

    public Unit(String category, String display, double factor, double offset) {
        this.category = category;
        this.display = display;
        this.factor = factor;
        this.offset = offset;
    }

    public static void convert(double value, String fromUnit, String toUnit) {
        
    }
}
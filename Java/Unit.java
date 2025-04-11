class Unit {
    private String display;
    private double factor;
    private double offset;

    public Unit(String display, double factor, double offset) {
        this.display = display;
        this.factor = factor;
        this.offset = offset;
    }

    public double getFactor() {
        return factor;
    }

    public double getOffset() {
        return offset;
    }

    public String getDisplay() {
        return display;
    }
}
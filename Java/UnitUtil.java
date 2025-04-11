public class UnitUtil {
    public static UnitUtil(){
        //load categories from json files
        Map<String, Category> categories = new HashMap<>();
        categories.put("Length", new Category("Length", new Unit("Meter", "m", 1, 0)));
        categories.put("Mass", new Category("Mass", new Unit("Kilogram", "kg", 1, 0)));
        categories.put("Time", new Category("Time", new Unit("Second", "s", 1, 0)));
        categories.put("Temperature", new Category("Temperature", new Unit("Celsius", "C", 1, 0)));
        categories.put("Electric Current", new Category("Electric Current", new Unit("Ampere", "A", 1, 0)));
    }
    public static void convert(String category, double value, String fromUnit, String toUnit) {
        // find fromUnit
        // find toUnit
        // if fromUnit is not base unit, convert toUnit to base
        // if toUnit is not base unit, convert base to toUnit and return result

    }
}
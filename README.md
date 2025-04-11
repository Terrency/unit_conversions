# unit_conversions
Use this library to convert between units of measurement.
units.json  is a json file that contains all the units of measurement.
conversion.json is a json file that contains the conversion factors between units of measurement.
other language folders contain the conversion code in other languages.

## Usage


## Units json
1. 第一版设计采用表达式执行单位间转换， 例如 meter_per_second = kilometer_per_hour / 3.6
2. 第二版借鉴了FMI的设计，factor默认值1.0， offset 默认值为0.0，例如 v_base = factor * v_unit + offset

```json 第一版
{
  "speed": {
    "base_unit": "meter_per_second",
    "meter_per_second": {
      "display": "m/s",
      "to_base": "value",
      "from_base": "value"
    },
    "kilometer_per_hour": {
      "display": "km/h",
      "to_base": "value / 3.6",
      "from_base": "value * 3.6"
    },
    "mile_per_hour": {
      "display": "mph",
      "to_base": "value / 2.23694",
      "from_base": "value * 2.23694"
    }
  }
}
```
 
```json 第二版
{
  "speed": {
    "base_unit": "meter_per_second",
    "meter_per_second": {
      "display": "m/s",
      "factor": 1
    },
    "kilometer_per_hour": {
      "display": "km/h",
      "factor": 3.6
    },
    "mile_per_hour": {
      "display": "mph",
      "factor": 2.23694
    }
  }
}
```
## Add a new units step by step
1. Open units.json
2. Add new Category
3. Add base_unit and units, make display, to_base, from_base

## Existing Units and category
| Category | Units |
| --- | --- |
| length | meter, kilometer, centimeter, millimeter, micrometer, nanometer, picometer, astronomical_unit, light_year, parsec, inch, foot, yard, mile, nautical_mile, fathom, furlong, fathom, league, nautical_mile, fathom, furlong, fathom, league, nautical_mile, fathom, furlong, fathom, league, nautical_mile, fathom, furlong, fathom, league, nautical_mile, fathom, furlong, fathom, league, na|
| weight | gram, kilogram, milligram, microgram, tonne, long_ton, short_ton, stone, pound, ounce, carat, atomic_mass_unit, dalton, electron_mass, proton_mass, neutron_mass, atomic_mass_unit, dalton, electron_mass, proton|
| volume | liter, milliliter, centiliter, deciliter, hectoliter, kiloliter, megaliter, cubic_meter, cubic_decimeter, cubic_centimeter, cubic_millimeter, cubic_kilometer, cubic_mile, cubic_yard|
| area | square_meter, square_centimeter, square_millimeter, square_kilometer, square_mile, square_yard, square_foot, square_inch, hectare,acre, square_mile, square_yard, square_foot, square_inch, hectare,acre, square_mile|
| temperature | celsius, fahrenheit, kelvin, rankine, reaumur, delisle, newton, roemer, ryder, reaumur, delisle, newton, roemer, ryder, reaumur, delisle, newton, roemer, ryder, reaumur, delisle, newton, roemer, ryder, reaumur, delisle, newton, roemer, ryder|
| speed | meter_per_second, kilometer_per_hour, mile_per_hour, knot, mach, speed_of_light, speed_of_sound, speed_of_sound_in_water, speed_of_sound_in_air, speed_of_sound_in_vacuum, speed_of_sound_in_steel, speed_of_sound_in_glass, speed_of_sound_in|
| acceleration | meter_per_second_squared, kilometer_per_hour_squared, mile_per_hour_squared, knot_squared, mach_squared, speed_of_light_squared, speed_of_sound_squared, speed_of_sound_in_water_squared, speed_of_sound|
| force | newton, kilogram_force, pound_force, kilopound_force, poundal, dyne, gram_force, kilogram_force, pound_force, kilopound_force, poundal, dyne, gram_force, kilogram_force, pound_force, kilopound_force, pound|
| energy | joule, kilojoule, megajoule, gigajoule, terajoule, petajoule, exajoule, zettajoule, yottajoule, electronvolt, kiloelectronvolt, megaelectronvolt, gigaelectronvolt, teraelectronvolt, petaelectronvolt, exaelectronvolt, zettaelectronvolt, yottaelectronvolt|
| power | watt, kilowatt, megawatt, gigawatt, terawatt, petawatt, exawatt, zettawatt, yottawatt, horsepower, kilohorsepower, megahorsepower, gigahorsepower, terahorsepower, petahorsepower, exahorsepower, zettahorsepower, yottahorsepower|
| pressure | pascal, kilopascal, megapascal, gigapascal, terapascal, petapascal, exapascal, zetapascal, yotapascal, bar, millibar, atmosphere, torr, psi, mmhg, atmosphere_standard, atmosphere_reduced, atmosphere_sea_level, atmosphere_standard, atmosphere_redu|
| time | second, minute, hour, day, week, month, year, decade, century, millennium, second, minute, hour, day, week, month, year, decade, century, millennium, second, minute, hour, day, week, month, year, decade, century, millennium, second, minute, hour, day, week, month, year, decade, century, millennium, second, minute, hour, day, week, month, year, decade, century, millennium, second, minute, hour, day, week, month, year, decade,century, millennium|
| angle | radian, degree, arcminute, arcsecond, gon, grad, minute, second, radian, degree, arcminute, arcsecond, gon, grad, minute, second, radian, degree, arcminute, arcsecond, gon, grad, minute, second, radian, degree, arcminute, arcsecond, gon, grad, minute, second, radian, degree, arcminute, arcsecond, gon, grad, minute, second, radian, degree, arcminute, arcsecond, gon, grad, minute, second, radian, degree, arcminute, arcsecond|
| mass | kilogram, gram, milligram, microgram, tonne, long_ton, short_ton, stone, pound, ounce, carat, atomic_mass_unit, dalton, electron_mass, proton_mass, neutron_mass, atomic_mass_unit, dalton, electron_mass, proton_mass, neutron_mass, atomic_mass_unit, dalton, electron_mass, proton_mass, neutron_mass, atomic_mass_unit, dalton, electron_mass|

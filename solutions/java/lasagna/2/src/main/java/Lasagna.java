public class Lasagna {
    private static final int EXPECTED_MINUTES_IN_OVEN = 40;
    private static final int MINUTES_TO_CREATE_LAYER = 2;
    public int expectedMinutesInOven(){
        return EXPECTED_MINUTES_IN_OVEN;
    }

    public int remainingMinutesInOven(int minutesInOven){
        return expectedMinutesInOven() - minutesInOven;
    }

    public int preparationTimeInMinutes(int numberOfLayers){
        return MINUTES_TO_CREATE_LAYER * numberOfLayers;
    }

    public int totalTimeInMinutes(int numberOfLayers, int minutesInOven){
        return preparationTimeInMinutes(numberOfLayers) + minutesInOven;
    }
}

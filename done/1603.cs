public class ParkingSystem {

    int bigSpaces;
    int mediumSpaces;
    int smallSpaces;

    public ParkingSystem(int big, int medium, int small) {
        this.bigSpaces = big;
        this.mediumSpaces = medium;
        this.smallSpaces = small;
    }
    
    public bool AddCar(int carType) {
        switch (carType)
        {
            case 1:
                this.bigSpaces--;
                return this.bigSpaces >= 0;
            case 2:
                this.mediumSpaces--;
                return this.mediumSpaces >= 0;
            case 3:
                this.smallSpaces--;
                return this.smallSpaces >= 0;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */
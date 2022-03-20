from scipy.interpolate import UnivariateSpline

class RegressionModelHandler:

    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")

    @staticmethod
    def getInterpolationFunctionBySpline(x,y,option=None):
        spl  = UnivariateSpline(x, y)
        spl.set_smoothing_factor(option[0])
        return spl

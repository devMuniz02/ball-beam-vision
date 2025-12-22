class PID {
public:
    PID(double kp, double ki, double kd);
    void setTunings(double kp, double ki, double kd);
    void setOutputLimits(double min, double max);
    void compute(double input, double setpoint);
    double getOutput();

private:
    double kp; // proportional gain
    double ki; // integral gain
    double kd; // derivative gain
    double integral; // integral term
    double lastError; // last error value
    double output; // output value
    double outputMin; // minimum output limit
    double outputMax; // maximum output limit;
};
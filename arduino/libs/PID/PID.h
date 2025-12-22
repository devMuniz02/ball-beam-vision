class PID {
public:
    PID(double kp, double ki, double kd);
    void setTunings(double kp, double ki, double kd);
    void setOutputLimits(double min, double max);
    void setMode(int mode);
    void compute();
    void reset();

    double getOutput() const;

    void setSetpoint(double setpoint);
    double getSetpoint() const;

    void setInput(double input);
    double getInput() const;

private:
    double kp; // proportional gain
    double ki; // integral gain
    double kd; // derivative gain

    double setpoint; // desired value
    double input;    // current value
    double output;   // output value

    double integral; // integral term
    double lastInput; // last input value

    double minOutput; // minimum output limit
    double maxOutput; // maximum output limit

    int mode; // mode (manual or automatic)
};
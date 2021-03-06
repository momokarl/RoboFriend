
#define PRINT_MOTORSPEED_MESSAGES 0
#define PRINT_SENSOR_MESSAGES     0

/* Motor pins right */
#define RightBackwardPin 10
#define RightForwardPin  11
#define RightPWMPin      14

/* Motor pins left */
#define LeftForwardPin   12
#define LeftBackwardPin  13
#define LeftPWMPin       15

#define STEPLENGTH      50
#define STEPLENGTH_TURN 20
#define ACCEL_STEP      2
#define MOVE_THRESHOLD  ACCEL_STEP*2

extern class Motor Motors;

class Motor {

public:
  Motor(void);
  ~Motor();

  void init();
  void stop();
  void drive (int left, int right, int duration);
  void updateMotors();

protected:

  int intendedRightSpeed;
  int intendedLeftSpeed;
  int intendedDuration;
  int rightSpeed;
  int leftSpeed;
  int handleObstacles();

};

class propulsion:
    def __init__(dataFromBase, index1):
        self.dataFromBase = dataFromBase
        self.index1 = index1

    def propulsionsystem():
        global mode,motorspeed1, motorspeed2, forward_left_motor, forward_right_motor, backward_left_motor, backward_right_motor;

        index2 = dataFromBase.index(',',index1+1)

        motorspeed = dataFromBase[index1+1:index2]
        a = strToInt(motorspeed)
        motorspeed1 = a
        motorspeed2 = a

        #print('motorspeed1',motorspeed1)
        motorspeed = dataFromBase[index2+1:]

        print(motorspeed)
        b = strToInt(motorspeed)

        motorspeed1 -= b
        motorspeed2 += b
        if (motorspeed1 > 100):
            motorspeed1 = 100
        elif (motorspeed1 < -100):
            motorspeed1 = -100

        if (motorspeed2 > 100):
            motorspeed2 = 100
        elif (motorspeed2 < -100):
            motorspeed2 = -100

        print('motorspeed1',motorspeed1)
        print('motorspeed2',motorspeed2)

        forward_left_motor.moveMotor(motorspeed2)
        backward_left_motor.moveMotor(motorspeed2)

        forward_right_motor.moveMotor(motorspeed1)
        backward_right_motor.moveMotor(motorspeed1)

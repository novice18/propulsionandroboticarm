def printRoboticArmVariables():
    print(baseMotorSpeed, baseActuator, armActuator, clawPitch, clawRoll, clawOpenClose)

def roboticArm(dataFromBase, index1):
    global baseMotorSpeed, baseActuator, armActuator, clawRoll, clawPitch, clawOpenClose;
    global Motor1_baseMotor, Motor2_baseActuator, Motor3_armActuator, Motor4_clawPitch, Motor5_clawRoll, Motor6_clawOpenClose;

    index2 = dataFromBase.index(',',index1+1)
    StrbaseMotorSpeed = dataFromBase[index1+1:index2]
    baseMotorSpeed = strToInt(StrbaseMotorSpeed);
    Motor1_baseMotor.moveMotor(baseMotorSpeed);
    Motor1_baseMotor.printMotor('Motor1_baseMotor');

    index3 = dataFromBase.index(',',index2+1)
    StrbaseActuator = dataFromBase[index2+1:index3]
    baseActuator = strToInt(StrbaseActuator);
    Motor2_baseActuator.moveMotor(baseActuator);
    Motor2_baseActuator.printMotor('Motor2_baseActuator');

    index4 = dataFromBase.index(',',index3+1)
    StrarmActuator = dataFromBase[index3+1:index4]
    armActuator = strToInt(StrarmActuator);
    Motor3_armActuator.moveMotor(armActuator);
    Motor3_armActuator.printMotor('Motor3_armActuator');

    index5 = dataFromBase.index(',',index4+1)
    StrclawPitch = dataFromBase[index4+1:index5]
    clawPitch = strToInt(StrclawPitch);
    Motor4_clawPitch.moveMotor(clawPitch);
    Motor4_clawPitch.printMotor('Motor4_clawPitch');

    index6 = dataFromBase.index(',',index5+1)
    StrclawRoll = dataFromBase[index5+1:index6]
    clawRoll = strToInt(StrclawRoll);
    Motor5_clawRoll.moveMotor(clawRoll);
    Motor5_clawRoll.printMotor('Motor5_clawRoll');

    StrclawOpenClose = dataFromBase[index6+1:]
    clawOpenClose = strToInt(StrclawOpenClose);
    Motor6_clawOpenClose.moveMotor(clawOpenClose);
    Motor6_clawOpenClose.printMotor('Motor6_clawOpenClose');

    printRoboticArmVariables();

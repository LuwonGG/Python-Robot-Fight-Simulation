# Name: Luan Vu
# Directory ID: LVu
# Due Date: 11/26/2018
# Description: Program simulates a game where robots on two teams battle each other.


class Robot:
    """
    A class for robot objects.
    """

    energy = 20

    def __init__(self, name=None):
        self.name = name
        self.compound = None

    def __add__(self, combo):
        """
        Creates a compound robot using itself and another "combo" robot.
        :param combo: <Robot> extra robot to combine with
        :return: CompoundRobot object
        """
        self.compound = CompoundRobot(self, combo)
        combo.compound = self.compound
        return self.compound

    def attack(self, target, energy_spent):
        """
        Robot attacks 'target' robot with the amount of energy_spent. The robot with the largest energy of the two
        robots, gains the energy amount and the other robot looses the energy amount. If the loosing robot doesn't have
        the energy amount, the winning robot only gains the amount of the loosing robot - 1. and the loosing robot
        looses all energy except 1. If the robots have the same amount of energy, the attacking robot will loose the
        energy amount and the "attacked" robot will remain the same.
        :param target: <Robot> robot being attacked (self is attacking robot)
        :param energy_spent: <float> amount of attack
        :return: none
        """
        if self.energy > target.energy:
            if target.energy >= energy_spent:
                self.energy += energy_spent
                target.energy -= energy_spent
            else:
                self.energy += (target.energy - 1)
                target.energy = 1
        elif target.energy > self.energy:
            if self.energy >= energy_spent:
                target.energy += energy_spent
                self.energy -= energy_spent
            else:
                target.energy += (target.energy - 1)
                self.energy = 1
        else:
            self.energy -= energy_spent


class CompoundRobot(Robot):
    """
    A child class of robot objects.
    """

    def __init__(self, robot1, robot2, *args, **kwargs):
        self.components = [robot1, robot2]
        self.energy = robot1.energy + robot2.energy
        self.compound = self
        # super(Robot, self).__init__(*args, **kwargs)

    def __iadd__(self, robot_added):
        """
        Adds a robot to the existing compound robot including its energy. Also appends to components list.
        :return: self
        """
        self.energy += robot_added.energy
        self.components.append(robot_added)
        self.compound = self
        robot_added.compound = self
        return self


if __name__ == "__main__":
    print("Welcome to the world of Robots!")

"""
BOOTCAMPERS TO COMPLETE.

Travel to designated waypoint.
"""

from .. import commands
from .. import drone_report

# Disable for bootcamp use
# pylint: disable-next=unused-import
from .. import drone_status
from .. import location
from ..private.decision import base_decision


# Disable for bootcamp use
# No enable
# pylint: disable=duplicate-code,unused-argument


class DecisionSimpleWaypoint(base_decision.BaseDecision):
    """
    Travel to the designed waypoint.
    """

    def __init__(self, waypoint: location.Location, acceptance_radius: float) -> None:
        """
        Initialize all persistent variables here with self.
        """
        self.waypoint = waypoint
        print(f"Waypoint: {waypoint}")

        self.acceptance_radius = acceptance_radius

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

    def run(
        self, report: drone_report.DroneReport, landing_pad_locations: "list[location.Location]"
    ) -> commands.Command:
        """
        Make the drone fly to the waypoint.

        You are allowed to create as many helper methods as you want,
        as long as you do not change the __init__() and run() signatures.

        This method will be called in an infinite loop, something like this:

        ```py
        while True:
            report, landing_pad_locations = get_input()
            command = Decision.run(report, landing_pad_locations)
            put_output(command)
        ```
        """
        # Default command
        command = commands.Command.create_null_command()

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============
        def distance_sqr(position: location.Location, destination: location.Location) -> float:
            pos_x = position.location_x
            pos_y = position.location_y
            des_x = destination.location_x
            des_y = destination.location_y

            return (pos_x - des_x) ** 2 + (pos_y - des_y) ** 2

        def in_radius(
            position: location.Location, destination: location.Location, radius: float
        ) -> bool:
            distance = distance_sqr(position, destination)
            return distance < radius**2

        if in_radius(report.position, self.waypoint, self.acceptance_radius):
            if report.status == drone_status.DroneStatus.HALTED:
                command = commands.Command.create_land_command()
            else:
                command = commands.Command.create_halt_command()
        else:
            relative_x = self.waypoint.location_x - report.position.location_x
            relative_y = self.waypoint.location_y - report.position.location_y
            command = commands.Command.create_set_relative_destination_command(
                relative_x, relative_y
            )
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

        return command

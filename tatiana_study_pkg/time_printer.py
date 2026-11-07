#!/usr/bin/env python3
import time

import rclpy
from rclpy.node import Node


class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')
        # период 5.0 секунд, при каждом срабатывании вызывается print_time
        self.timer = self.create_timer(5.0, self.print_time)

    def print_time(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        self.get_logger().info(f'Текущее время: {now}')


def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


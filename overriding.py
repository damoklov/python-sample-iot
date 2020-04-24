from multimethod import multimethod
import doctest


class WithStaticAndOverload:

    worker_name = "Worker"

    @staticmethod
    def do_work():
        """
        >>> WithStaticAndOverload.do_work()
        'Worker'
        """
        return WithStaticAndOverload.worker_name

    def sing_a_song(self):
        """
        >>> obj.sing_a_song()
        Worker
        """
        print(WithStaticAndOverload.do_work())

    @multimethod
    def print_data(self, first, second):
        """
        >>> obj.print_data("11", "12")
        '1112'
        """
        return str(first) + str(second)

    @multimethod
    def print_data(self, first, second):
        """
        >>> obj.print_data(11, 12)
        '23'
        """
        return str(first + second)


if __name__ == '__main__':
    doctest.testmod(verbose=True, extraglobs={'obj': WithStaticAndOverload()})

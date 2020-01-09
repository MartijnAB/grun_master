rom __future__ import annotations
from abc import ABC, abstractmethod

__author__ = "Rolf Vedder"
"""
    Copyright (C) 2019  R.H.J. Vedder [rolf.vedder@gmail.com]

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class Graph(ABC):
    """
    The Graph class declares the factory method that is supposed to return an
    object of a Plot class. The Graph's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Graph Factory may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Graph's primary responsibility
        is not creating plots. Usually, it contains some core business logic
        that relies on Plot objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of plot from it.
        """

        # Call the factory method to create a Plot object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Graph: The same graph's code has just worked with {product.operation()}"

        return result


"""
Graph's subclasses override the factory method in order to change the resulting
plot's type.
"""


class LineGraph(Graph):
    """
    Note that the signature of the method still uses the abstract plot type,
    even though the plot type is actually returned from the method. This
    way the Graph Factory can stay independent of plot classes.
    """

    def factory_method(self) -> Line:
        return Line()


class BarGraph(Graph):
    def factory_method(self) -> Bar:
        return Bar()


class Plot(ABC):
    """
    The Plot interface declares the operations that all plots
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Plots provide various implementations of the Plot interface.
"""


class Line(Plot):
    def operation(self) -> str:
        return "{Result of the Line}"


class Bar(Plot):
    def operation(self) -> str:
        return "{Result of the Bar}"


def show_Graph(creator: Graph) -> None:
    """
    The client code works with an instance of a Graph, albeit through
    its base interface. As long as the client keeps working with the graph factory via
    the base interface, you can pass it any graph's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Showing a lineGraph.")
    show_Graph(LineGraph())
    print("\n")

    print("App: Showing a BarGraph.")
    show_Graph(BarGraph())

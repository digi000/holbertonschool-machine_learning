#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jordan Tuyisnge
"""


class Poisson:
    """
    Representing a Poisson distribution
    """

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor

        Arguments:
        - data (list): is a list of the data to be used to estimate the
        distribution
        - lambtha (int/float): is the expected number of occurences
        in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        '''Calculates PMF '''
        if k < 0:
            # print('evaluo k')
            return 0
        k = int(k)
        e = 2.7182818285
        factorial = 1
        for i in range(1, int(k) + 1):
            factorial = factorial * i

        return (pow(e, -self.lambtha) * (pow(self.lambtha, k)) / factorial)


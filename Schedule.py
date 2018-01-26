"""
MIT License

Copyright (c) 2018 Aykut Akin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = 'Aykut Akin'

import random

class Schedule:

    def __init__(self, person_list):
        self.__person_list = person_list
        self.__person_score_dict = dict()
        for person in self.__person_list:
            self.__person_score_dict[person] = 0

    def __get_min_scored_person(self, do_not_include_list):
        min_score = min(self.__person_score_dict.values())
        min_scored_person_list = [key for key, v in self.__person_score_dict.items()
                                  if v == min_score and key not in do_not_include_list]
        choice_of_min_person = min_scored_person_list.pop(random.randint(0, min_scored_person_list.__len__()-1))
        self.__person_score_dict[choice_of_min_person] = min_score+1
        return choice_of_min_person

    def print_schedule(self, times, pair_count):
        prev_pair = list()
        for i in range(times):
            selected_pair = list()
            for j in range(pair_count):
                selected_pair.append(self.__get_min_scored_person(prev_pair + selected_pair))
            prev_pair = selected_pair
            print(selected_pair)
        print(self.__person_score_dict)

def main():
    schedule = Schedule({'AYDAN', 'AYKUT', 'CAN', 'CANBURAK', 'ECE', 'GIZEM', 'GOZDEGUL', 'MEHMET', 'MUGE', 'YASIN'})
    schedule.print_schedule(10, 2)

if __name__ == '__main__':
    main()

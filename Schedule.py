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
    schedule.print_schedule(10, 5)

if __name__ == '__main__':
    main()

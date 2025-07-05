# def main():
#     names = ["lukas", "sada", "adada"]
#     names_to_length = convert_list_to_dictionary(names)
#     print(names_to_length)
#
# def convert_list_to_dictionary(names):
#     return {name: len(name) for name in names}
#
# main()


# from operator import itemgetter
#
# names_to_scores = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
#
# name_width = len(max(list(names_to_scores.keys()),key=len))
# score_width = max([len(str(score)) for score in names_to_scores.values()])
#
# for name, score in sorted(names_to_scores.items(), key=itemgetter(1), reverse=True):
#     print(f"{name:{name_width}} = {score:{score_width}}")
import math
def check_pnr (pnr_list=[]):
    """
    Kollar om kontrollnumret i ett personnummer stämmer.
    :param pnr_list: Personnummer
    :type pnr_list: [Number]
    :return:
    """
    sum=0
    control_pnr= pnr_list[len(pnr_list)-1]          # Drar ut kontrollnumret ur personnumret
    for n in range(len(pnr_list)-1):                # Alla förutom kontrollnumret
        multiplier = 2 - n%2                        # Första multipliceras med 2, sen 1,2...
        sum+= multiplier * pnr_list[n]
    rounded_sum = int(math.ceil(sum/10.0)*10)       # 22->2.2->3.0->30
    calc_pnr = (rounded_sum - sum)                  # Jämförs med kontrollnumret i listan
    return calc_pnr == control_pnr

personal_id_ok = [7, 4, 0, 2, 1, 7, 4, 8, 2, 0]
personal_id_fail = [7, 4, 0, 2, 1, 7, 4, 8, 2, 1]
print(check_pnr(personal_id_fail))
print(check_pnr(personal_id_ok))
check_pnr()
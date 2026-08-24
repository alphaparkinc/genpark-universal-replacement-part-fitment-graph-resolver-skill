from client import UniversalReplacementPartFitmentGraphResolverClient

def main():
    client = UniversalReplacementPartFitmentGraphResolverClient()
    res = client.verify_part_fitment('04465-02220', '10842')
    print('Part: ' + res['part_oem_number'] + ' (' + res['part_category'] + ')')
    print('Fitment: ' + res['fitment_guarantee'] + ' on ' + res['target_vehicle'] + ' (' + str(res['confidence_score']*100) + '%)')
    print('Interchangeable: ' + str(res['interchangeable_aftermarket_skus']))

if __name__ == '__main__':
    main()

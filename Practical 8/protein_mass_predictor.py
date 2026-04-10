aa_mass = {"G": 57.02,"A": 71.04,"S": 87.03,"P": 97.05,"V": 99.07,"T": 101.05,"C": 103.01,"I": 113.08,"L": 113.08,"N": 114.04,"D": 115.03,"Q": 128.06,"K": 128.09,"E": 129.04,"M": 131.04,"H": 137.06,"F": 147.07,"R": 156.10,"Y": 163.06,"W": 186.08}
def calculate_protein_mass(sequence):
    """
    calculate the total molecular mass of a protein sequence in atomic mass units(amu)
    Args:
        sequence:A string of single-letter amino acid codes (e.g., 'AGCT')
    Returns:
        Total mass (float) if all amino acids are valid,otherwise returns None
    Example:
        calculate_protein_mass('AG')
        128.06  # 57.02+71.04
    """
    total=0
    for aa in sequence:
        if aa not in aa_mass:
            print(f'Invalid amino acid: {aa}')
            return None
        total+=aa_mass[aa]
    return total
#example function call
print ('Please input amino acid sequence:')
user_input=input()
result=calculate_protein_mass(user_input)
if result is not None:
    print(f'Total mass:{result} amu')

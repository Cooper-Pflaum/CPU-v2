import argparse

instructions = ['NOP', 'AIN', 'BIN', 'CIN', 'LDIA', 'LDIB', 'RDEXP', 'WREXP', 'STA', 'STC', 'ADD', 'SUB', 'MULT', 'DIV', 'JMP', 'JMPZ', 'JMPC', 'LDAIN', 'STAOUT', 'SWP', 'SWPC', 'HLT', 'WRDSP', 'WRX', 'WRY']

def convert_file(input_file, output_file):
    PGRM = []
    PGRM_RAW = []
    try:
        with open(input_file, 'r') as f_in:

            # reading each line    
            for line in f_in:
                line = line.split('//')[0]

                # reading each word        
                for word in line.split():

                    PGRM.append(word)
                    try:
                        index = format(instructions.index(word), '04x')
                        PGRM_RAW.append(index)
                    except ValueError:
                        PGRM_RAW.append(word)
        while len(PGRM_RAW) < 65535:
            PGRM_RAW.append('0000')  # Insert blank instructions

        with open(output_file, 'w') as f_out:
            f_out.write('v3.0 hex words addressed')

            CURR_INSTR = 0
            for INSTR in PGRM_RAW:
                if(CURR_INSTR % 0x10 == 0):
                    f_out.write('\n' + format(CURR_INSTR, '04x') + ": ")
                f_out.write(INSTR + ' ')
                CURR_INSTR+=1;

            print(f"File {input_file} converted successfully")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assembly to machine code program")
    parser.add_argument("-r", "--input", help="Input file to read", required=True)
    parser.add_argument("-o", "--output", help="Output file to write to", required=True)
    args = parser.parse_args()
    convert_file(args.input, args.output)


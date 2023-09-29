def split_file(input_file, lines_per_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    num_files = len(lines) // lines_per_file

    for i in range(num_files + 1):
        start_idx = i * lines_per_file
        end_idx = (i + 1) * lines_per_file
        output_file = f'file_name{i}.ts'

        with open(output_file, 'w') as file:
            file.write('import { SeedName } from \'@prisma/client\';\n\n')
            file.write(f'export const seedName{i}: SeedName[] = [\n')
            file.writelines(lines[start_idx:end_idx])
            file.write('];\n')


split_file('/split-script/squema.ts', 666)

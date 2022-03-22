from subprocess import check_output

def run_cmd(cmd):
    exclude, include = [], []
    if len(exclude) > 0:
        cmd += ' --exclude ' + ' --exclude '.join(exclude)
    if len(include) > 0:
        cmd += ' --include ' + ' --include '.join(include)

    print(f'running {cmd}')
    out = check_output(cmd.split(' '))
    print(f'output:\n {out}')

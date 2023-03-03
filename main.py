import helpers
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', required=True)
args = parser.parse_args()


if __name__ == '__main__':

    ami_id = str(args.name)
    res_launch = helpers.launch_template(ami_id)
    print('Launch Config status:', res_launch)
    res_autoscale = helpers.update_autoscaling('VUS-PROD-APP')
    print('autoscaling status:', res_autoscale)
    res_refresh = helpers.instance_refresh()
    print('Refresh status:', res_autoscale)

#Assignment 3 - uebercool command

export PORTALNAME=name
export PROJECTID=fg465

ssh india
#type in password
ssh -l ubuntu -i ~/.ssh/$PORTALNAME-001 10.23.0.176
virtualenv ~/ENV2
source ~/ENV2/bin/activate
pip install --upgrade pip
pip --trusted-host pypi.python.org install cloudmesh_base
pip --trusted-host pypi.python.org install cmd3
pip search --trusted-host pypi.python.org autopep8 pylint
which cm
cm help
nano ~/.cloudmesh/cmd3.yaml
#create a .pu file contains:
#meta:
#    yaml_version: 2.1
#    kind: cmd3
#    filename: ${HOME}/.cloudmesh/cmd3.yaml
#    location: ${HOME}/.cloudmesh/cmd3.yaml
#    prefix: null
#cmd3:
#    modules:
#    - cloudmesh_cmd3.plugins
#    - cloudmesh_docker.plugins
#    - cloudmesh_slurm.plugins
#    - cloudmesh_deploy.plugins
cm-generate-command
cm-generate-command uebercool --path=~
cd ~/cloudmesh_uebercool
python setup.py install
emacs ~/.cloudmesh/cmd3.yaml
#edit the yaml file to add the new custom command
cm
help

#Exercise1
cm-generate-command your command --path=~
cd ~/cloudmesh_your_command
python setup.py install
cm
help
cm your command deploy $filename






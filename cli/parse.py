"""
Parses the pvtrace-scene.yml file and generates Python objects.
"""
import jsonschema
import yaml
import json
import os
import typer
from pvtrace import *
from types import SimpleNamespace

SCHEMA = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "pvtrace-schema-scene-spec.json"
)


def load_schema():
    print(SCHEMA)
    with open(SCHEMA, "r") as fp:
        schema = json.load(fp)
        jsonschema.Draft7Validator.check_schema(schema)
        return schema


def load_spec(filename):
    """Load user's scene specification file."""
    with open(filename, "r") as fp:
        spec = yaml.load(fp, Loader=yaml.Loader)
        return spec


def parse(filename):
    schema = load_schema()
    spec = load_spec(filename)
    jsonschema.validate(spec, schema=schema)
    schema_version = spec["version"]
    if schema_version == "1.0":
        return parse_v_1_0(spec)
    else:
        raise ValueError("Version {} not supported".format(schema_version))


def parse_v_1_0(spec):
    print(spec['nodes']['world'])
    x = json.loads(json.dumps(spec), object_hook=lambda d: SimpleNamespace(**d))
    print(x.nodes.world)
    world = json.loads(json.dumps(spec['nodes']['world']), object_hook=lambda d: Node(**d))
    # print(world)

    # world = Node(
    #     name = "world (air)"
    # )
    # if hasattr(x.nodes.world, 'box'):
    #     world.geometry = Box(
    #         size = x.nodes.world.box.size,
    #         material = Material(refractive_index=getattr(x.nodes.world.box.material,'refractive-index'))
    #     )



def main(scene: typer.FileText = typer.Option(...)):
    scene_spec = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), scene.name
    )
    parse(scene_spec)

if __name__ == "__main__":
    typer.run(main)

    print("OK")

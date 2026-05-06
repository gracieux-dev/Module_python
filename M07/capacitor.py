from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.factory import CreatureFactory
from ex1.heal import HealCapability
from ex1.transform import TransformCapability


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print("base:")
    print(base.describe())
    print(base.attack())
    assert isinstance(base, HealCapability)
    print(base.heal())
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    assert isinstance(evolved, HealCapability)
    print(evolved.heal())


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    evolved = factory.create_evolved()
    assert isinstance(base, TransformCapability)
    assert isinstance(evolved, TransformCapability)
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(healing_factory)
    test_transform(transform_factory)

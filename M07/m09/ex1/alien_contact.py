from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    EMERGENCY = "emergency"
    ROUTINE = "routine"
    SCIENTIFIC = "scientific"
    MAINTENANCE = "maintenance"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include received messages")

        return self


if __name__ == "__main__":
    print("Alien Contact Data Validation")
    print("=" * 40)

    contact = AlienContact(
        contact_id="AC001",
        timestamp=datetime.now(),
        location="Roswell, New Mexico",
        contact_type=ContactType.TELEPATHIC,
        signal_strength=6.5,
        duration_minutes=30,
        witness_count=5,
        message_received=None,
        is_verified=True,
    )

    print("Valid contact created:")
    print(f"ID: {contact.contact_id}")
    print(f"Location: {contact.location}")
    print(f"Type: {contact.contact_type.value.capitalize()}")
    print(f"Signal Strength: {contact.signal_strength}")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Verified: {contact.is_verified}")
    print("=" * 40)

    test_cases = [
        (
            "Invalid prefix",
            dict(
                contact_id="XX001",
                timestamp=datetime.now(),
                location="Area 51",
                contact_type=ContactType.ROUTINE,
                signal_strength=5.0,
                duration_minutes=10,
                witness_count=2,
                is_verified=False,
            ),
        ),
        (
            "Unverified physical contact",
            dict(
                contact_id="AC002",
                timestamp=datetime.now(),
                location="Nevada Desert",
                contact_type=ContactType.PHYSICAL,
                signal_strength=4.0,
                duration_minutes=15,
                witness_count=2,
                is_verified=False,
            ),
        ),
        (
            "Telepathic with too few witnesses",
            dict(
                contact_id="AC003",
                timestamp=datetime.now(),
                location="Pacific Ocean",
                contact_type=ContactType.TELEPATHIC,
                signal_strength=3.0,
                duration_minutes=20,
                witness_count=2,
                is_verified=True,
            ),
        ),
        (
            "Strong signal without message",
            dict(
                contact_id="AC004",
                timestamp=datetime.now(),
                location="Antarctica",
                contact_type=ContactType.SCIENTIFIC,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=3,
                message_received=None,
                is_verified=True,
            ),
        ),
    ]

    for label, data in test_cases:
        try:
            AlienContact(**data)
        except ValidationError as e:
            print(f"Expected error — {label}:")
            for error in e.errors():
                print(f"  {error['msg']}")
            print("=" * 40)

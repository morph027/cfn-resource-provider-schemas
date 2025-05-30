SCHEMA = {
  "typeName" : "AWS::Shield::ProactiveEngagement",
  "description" : "Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-shield.git",
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "readOnlyProperties" : [ "/properties/AccountId" ],
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False,
  "required" : [ "ProactiveEngagementStatus", "EmergencyContactList" ],
  "properties" : {
    "AccountId" : {
      "type" : "string"
    },
    "ProactiveEngagementStatus" : {
      "description" : "If `ENABLED`, the Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.\nIf `DISABLED`, the SRT will not proactively notify contacts about escalations or to initiate proactive customer support.",
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "EmergencyContactList" : {
      "description" : "A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support.\nTo enable proactive engagement, the contact list must include at least one phone number.",
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 10,
      "items" : {
        "$ref" : "#/definitions/EmergencyContact"
      }
    }
  },
  "definitions" : {
    "EmergencyContact" : {
      "description" : "An emergency contact is used by Shield Response Team (SRT) to contact you for escalations to the SRT and to initiate proactive customer support. An emergency contact requires an email address.",
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "EmailAddress" ],
      "properties" : {
        "ContactNotes" : {
          "description" : "Additional notes regarding the contact.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1024,
          "pattern" : "^[\\w\\s\\.\\-,:/()+@]*$"
        },
        "EmailAddress" : {
          "description" : "The email address for the contact.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 150,
          "pattern" : "^\\S+@\\S+\\.\\S+$"
        },
        "PhoneNumber" : {
          "description" : "The phone number for the contact",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 16,
          "pattern" : "^\\+[1-9]\\d{1,14}$"
        }
      }
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "shield:DescribeSubscription", "shield:DescribeEmergencyContactSettings", "shield:AssociateProactiveEngagementDetails", "shield:UpdateEmergencyContactSettings", "shield:EnableProactiveEngagement" ]
    },
    "delete" : {
      "permissions" : [ "shield:DescribeSubscription", "shield:DescribeEmergencyContactSettings", "shield:UpdateEmergencyContactSettings", "shield:DisableProactiveEngagement" ]
    },
    "read" : {
      "permissions" : [ "shield:DescribeSubscription", "shield:DescribeEmergencyContactSettings" ]
    },
    "update" : {
      "permissions" : [ "shield:DescribeSubscription", "shield:DescribeEmergencyContactSettings", "shield:UpdateEmergencyContactSettings", "shield:EnableProactiveEngagement", "shield:DisableProactiveEngagement" ]
    },
    "list" : {
      "permissions" : [ "shield:DescribeSubscription", "shield:DescribeEmergencyContactSettings" ]
    }
  }
}
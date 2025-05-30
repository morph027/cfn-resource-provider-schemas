SCHEMA = {
  "typeName" : "AWS::GuardDuty::Master",
  "description" : "GuardDuty Master resource schema",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-guardduty.git",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "MasterId" : {
      "description" : "ID of the account used as the master account.",
      "type" : "string"
    },
    "InvitationId" : {
      "description" : "Value used to validate the master account to the member account.",
      "type" : "string"
    },
    "DetectorId" : {
      "description" : "Unique ID of the detector of the GuardDuty member account.",
      "type" : "string"
    }
  },
  "required" : [ "MasterId", "DetectorId" ],
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/MasterId", "/properties/InvitationId", "/properties/DetectorId" ],
  "primaryIdentifier" : [ "/properties/DetectorId", "/properties/MasterId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "guardduty:ListInvitations", "guardduty:AcceptInvitation", "guardduty:GetMasterAccount" ]
    },
    "read" : {
      "permissions" : [ "guardduty:GetMasterAccount" ]
    },
    "delete" : {
      "permissions" : [ "guardduty:DisassociateFromMasterAccount" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DetectorId" : {
            "type" : "string"
          },
          "MasterId" : {
            "type" : "string"
          }
        }
      },
      "permissions" : [ "guardduty:GetMasterAccount" ]
    }
  }
}
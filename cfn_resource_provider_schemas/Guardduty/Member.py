SCHEMA = {
  "typeName" : "AWS::GuardDuty::Member",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-guardduty",
  "description" : "Resource Type definition for AWS::GuardDuty::Member",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "Status" : {
      "type" : "string"
    },
    "MemberId" : {
      "type" : "string"
    },
    "Email" : {
      "type" : "string"
    },
    "Message" : {
      "type" : "string"
    },
    "DisableEmailNotification" : {
      "type" : "boolean"
    },
    "DetectorId" : {
      "type" : "string"
    }
  },
  "required" : [ "Email" ],
  "primaryIdentifier" : [ "/properties/DetectorId", "/properties/MemberId" ],
  "createOnlyProperties" : [ "/properties/DetectorId", "/properties/MemberId" ],
  "writeOnlyProperties" : [ "/properties/DisableEmailNotification", "/properties/Message" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "guardduty:CreateMembers", "guardduty:GetMembers" ]
    },
    "read" : {
      "permissions" : [ "guardduty:GetMembers" ]
    },
    "delete" : {
      "permissions" : [ "guardduty:GetMembers", "guardduty:DisassociateMembers", "guardduty:DeleteMembers" ]
    },
    "update" : {
      "permissions" : [ "guardduty:GetMembers", "guardduty:CreateMembers", "guardduty:DisassociateMembers", "guardduty:StartMonitoringMembers", "guardduty:StopMonitoringMembers", "guardduty:InviteMembers" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DetectorId" : {
            "type" : "string"
          }
        }
      },
      "permissions" : [ "guardduty:ListMembers" ]
    }
  }
}
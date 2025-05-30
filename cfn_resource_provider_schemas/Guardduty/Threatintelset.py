SCHEMA = {
  "typeName" : "AWS::GuardDuty::ThreatIntelSet",
  "description" : "Resource Type definition for AWS::GuardDuty::ThreatIntelSet",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-guardduty",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "guardduty:TagResource", "guardduty:UntagResource", "guardduty:ListTagsForResource" ]
  },
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Format" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 300
    },
    "Activate" : {
      "type" : "boolean"
    },
    "DetectorId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 32
    },
    "Name" : {
      "type" : "string"
    },
    "Location" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 300
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/TagItem"
      }
    }
  },
  "definitions" : {
    "TagItem" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "required" : [ "Format", "Location" ],
  "primaryIdentifier" : [ "/properties/Id", "/properties/DetectorId" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/Format", "/properties/DetectorId" ],
  "writeOnlyProperties" : [ "/properties/Activate" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "guardduty:CreateThreatIntelSet", "guardduty:GetThreatIntelSet", "guardduty:TagResource", "iam:PutRolePolicy" ]
    },
    "read" : {
      "permissions" : [ "guardduty:GetThreatIntelSet" ]
    },
    "delete" : {
      "permissions" : [ "guardduty:ListDetectors", "guardduty:ListThreatIntelSets", "guardduty:DeleteThreatIntelSet", "guardduty:GetThreatIntelSet", "iam:DeleteRolePolicy" ]
    },
    "update" : {
      "permissions" : [ "guardduty:UpdateThreatIntelSet", "guardduty:GetThreatIntelSet", "guardduty:ListThreatIntelSets", "iam:PutRolePolicy", "guardduty:TagResource", "guardduty:UntagResource" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DetectorId" : {
            "type" : "string"
          }
        }
      },
      "permissions" : [ "guardduty:ListThreatIntelSets" ]
    }
  }
}
SCHEMA = {
  "typeName" : "AWS::SSMContacts::Contact",
  "description" : "Resource Type definition for AWS::SSMContacts::Contact",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "The value for the tag.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "ContactTargetInfo" : {
      "type" : "object",
      "description" : "The contact that SSM Incident Manager is engaging during an incident.",
      "properties" : {
        "ContactId" : {
          "description" : "The Amazon Resource Name (ARN) of the contact.",
          "type" : "string"
        },
        "IsEssential" : {
          "type" : "boolean",
          "description" : "A Boolean value determining if the contact's acknowledgement stops the progress of stages in the plan."
        }
      },
      "required" : [ "ContactId", "IsEssential" ],
      "additionalProperties" : False
    },
    "ChannelTargetInfo" : {
      "type" : "object",
      "description" : "Information about the contact channel that SSM Incident Manager uses to engage the contact.",
      "properties" : {
        "ChannelId" : {
          "description" : "The Amazon Resource Name (ARN) of the contact channel.",
          "type" : "string"
        },
        "RetryIntervalInMinutes" : {
          "type" : "integer",
          "description" : "The number of minutes to wait to retry sending engagement in the case the engagement initially fails."
        }
      },
      "required" : [ "ChannelId", "RetryIntervalInMinutes" ],
      "additionalProperties" : False
    },
    "Stage" : {
      "description" : "A set amount of time that an escalation plan or engagement plan engages the specified contacts or contact methods.",
      "type" : "object",
      "properties" : {
        "DurationInMinutes" : {
          "description" : "The time to wait until beginning the next stage.",
          "type" : "integer"
        },
        "Targets" : {
          "type" : "array",
          "description" : "The contacts or contact methods that the escalation plan or engagement plan is engaging.",
          "items" : {
            "$ref" : "#/definitions/Targets"
          }
        },
        "RotationIds" : {
          "type" : "array",
          "description" : "List of Rotation Ids to associate with Contact",
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        }
      },
      "oneOf" : [ {
        "required" : [ "DurationInMinutes" ]
      }, {
        "required" : [ "RotationIds" ]
      } ],
      "additionalProperties" : False
    },
    "Targets" : {
      "description" : "The contacts or contact methods that the escalation plan or engagement plan is engaging.",
      "type" : "object",
      "properties" : {
        "ContactTargetInfo" : {
          "$ref" : "#/definitions/ContactTargetInfo"
        },
        "ChannelTargetInfo" : {
          "$ref" : "#/definitions/ChannelTargetInfo"
        }
      },
      "additionalProperties" : False,
      "oneOf" : [ {
        "required" : [ "ChannelTargetInfo" ]
      }, {
        "required" : [ "ContactTargetInfo" ]
      } ]
    }
  },
  "properties" : {
    "Alias" : {
      "description" : "Alias of the contact. String value with 20 to 256 characters. Only alphabetical, numeric characters, dash, or underscore allowed.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "^[a-z0-9_\\-\\.]*$"
    },
    "DisplayName" : {
      "description" : "Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "^[a-zA-Z0-9_\\-\\s]*$"
    },
    "Type" : {
      "description" : "Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.",
      "type" : "string",
      "enum" : [ "PERSONAL", "ESCALATION", "ONCALL_SCHEDULE" ]
    },
    "Plan" : {
      "description" : "The stages that an escalation plan or engagement plan engages contacts and contact methods in.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Stage"
      }
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the contact."
    }
  },
  "additionalProperties" : False,
  "required" : [ "Alias", "DisplayName", "Type" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/Plan" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Alias", "/properties/Type" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ssm-contacts:TagResource", "ssm-contacts:UntagResource", "ssm-contacts:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ssm-contacts:CreateContact", "ssm-contacts:GetContact", "ssm-contacts:AssociateContact", "ssm-contacts:TagResource", "ssm-contacts:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "ssm-contacts:GetContact", "ssm-contacts:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "ssm-contacts:UpdateContact", "ssm-contacts:GetContact", "ssm-contacts:AssociateContact", "ssm-contacts:TagResource", "ssm-contacts:UntagResource", "ssm-contacts:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "ssm-contacts:DeleteContact", "ssm-contacts:GetContact", "ssm-contacts:AssociateContact" ]
    },
    "list" : {
      "permissions" : [ "ssm-contacts:ListContacts", "ssm-contacts:ListTagsForResource" ]
    }
  }
}
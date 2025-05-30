SCHEMA = {
  "typeName" : "AWS::SSMContacts::Plan",
  "description" : "Engagement Plan for a SSM Incident Manager Contact.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
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
          "insertionOrder" : False,
          "description" : "The contacts or contact methods that the escalation plan or engagement plan is engaging.",
          "items" : {
            "$ref" : "#/definitions/Targets"
          }
        }
      },
      "required" : [ "DurationInMinutes" ],
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
    "ContactId" : {
      "description" : "Contact ID for the AWS SSM Incident Manager Contact to associate the plan.",
      "type" : "string",
      "pattern" : "arn:[-\\w+=\\/,.@]+:[-\\w+=\\/,.@]+:[-\\w+=\\/,.@]*:[0-9]+:([\\w+=\\/,.@:-]+)*"
    },
    "Stages" : {
      "description" : "The stages that an escalation plan or engagement plan engages contacts and contact methods in.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Stage"
      }
    },
    "RotationIds" : {
      "description" : "Rotation Ids to associate with Oncall Contact for engagement.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Arn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the contact."
    }
  },
  "additionalProperties" : False,
  "oneOf" : [ {
    "required" : [ "ContactId", "Stages" ]
  }, {
    "required" : [ "ContactId", "RotationIds" ]
  } ],
  "createOnlyProperties" : [ "/properties/ContactId" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/RotationIds" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ssm-contacts:UpdateContact", "ssm-contacts:GetContact", "ssm-contacts:AssociateContact" ]
    },
    "read" : {
      "permissions" : [ "ssm-contacts:GetContact" ]
    },
    "update" : {
      "permissions" : [ "ssm-contacts:UpdateContact", "ssm-contacts:GetContact", "ssm-contacts:AssociateContact" ]
    },
    "delete" : {
      "permissions" : [ "ssm-contacts:UpdateContact", "ssm-contacts:GetContact", "ssm-contacts:AssociateContact" ]
    }
  }
}
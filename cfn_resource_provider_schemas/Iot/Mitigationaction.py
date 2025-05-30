SCHEMA = {
  "typeName" : "AWS::IoT::MitigationAction",
  "description" : "Mitigation actions can be used to take actions to mitigate issues that were found in an Audit finding or Detect violation.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iot.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The tag's key.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The tag's value.",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    },
    "ActionParams" : {
      "type" : "object",
      "description" : "The set of parameters for this mitigation action. You can specify only one type of parameter (in other words, you can apply only one action for each defined mitigation action).",
      "properties" : {
        "AddThingsToThingGroupParams" : {
          "$ref" : "#/definitions/AddThingsToThingGroupParams"
        },
        "EnableIoTLoggingParams" : {
          "$ref" : "#/definitions/EnableIoTLoggingParams"
        },
        "PublishFindingToSnsParams" : {
          "$ref" : "#/definitions/PublishFindingToSnsParams"
        },
        "ReplaceDefaultPolicyVersionParams" : {
          "$ref" : "#/definitions/ReplaceDefaultPolicyVersionParams"
        },
        "UpdateCACertificateParams" : {
          "$ref" : "#/definitions/UpdateCACertificateParams"
        },
        "UpdateDeviceCertificateParams" : {
          "$ref" : "#/definitions/UpdateDeviceCertificateParams"
        }
      },
      "additionalProperties" : False
    },
    "AddThingsToThingGroupParams" : {
      "description" : "Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.",
      "type" : "object",
      "properties" : {
        "OverrideDynamicGroups" : {
          "type" : "boolean",
          "description" : "Specifies if this mitigation action can move the things that triggered the mitigation action out of one or more dynamic thing groups."
        },
        "ThingGroupNames" : {
          "description" : "The list of groups to which you want to add the things that triggered the mitigation action.",
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 128
          },
          "minItems" : 1,
          "maxItems" : 10,
          "insertionOrder" : False
        }
      },
      "required" : [ "ThingGroupNames" ],
      "additionalProperties" : False
    },
    "EnableIoTLoggingParams" : {
      "description" : "Parameters to define a mitigation action that enables AWS IoT logging at a specified level of detail.",
      "type" : "object",
      "properties" : {
        "LogLevel" : {
          "type" : "string",
          "enum" : [ "DEBUG", "INFO", "ERROR", "WARN", "UNSET_VALUE" ],
          "description" : " Specifies which types of information are logged."
        },
        "RoleArnForLogging" : {
          "description" : " The ARN of the IAM role used for logging.",
          "type" : "string",
          "minLength" : 20,
          "maxLength" : 2048
        }
      },
      "required" : [ "LogLevel", "RoleArnForLogging" ],
      "additionalProperties" : False
    },
    "PublishFindingToSnsParams" : {
      "type" : "object",
      "description" : "Parameters, to define a mitigation action that publishes findings to Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.",
      "properties" : {
        "TopicArn" : {
          "type" : "string",
          "description" : "The ARN of the topic to which you want to publish the findings.",
          "minLength" : 20,
          "maxLength" : 2048
        }
      },
      "required" : [ "TopicArn" ],
      "additionalProperties" : False
    },
    "ReplaceDefaultPolicyVersionParams" : {
      "type" : "object",
      "description" : "Parameters to define a mitigation action that adds a blank policy to restrict permissions.",
      "properties" : {
        "TemplateName" : {
          "type" : "string",
          "enum" : [ "BLANK_POLICY", "UNSET_VALUE" ]
        }
      },
      "required" : [ "TemplateName" ],
      "additionalProperties" : False
    },
    "UpdateCACertificateParams" : {
      "type" : "object",
      "description" : "Parameters to define a mitigation action that changes the state of the CA certificate to inactive.",
      "properties" : {
        "Action" : {
          "type" : "string",
          "enum" : [ "DEACTIVATE", "UNSET_VALUE" ]
        }
      },
      "required" : [ "Action" ],
      "additionalProperties" : False
    },
    "UpdateDeviceCertificateParams" : {
      "type" : "object",
      "description" : "Parameters to define a mitigation action that changes the state of the device certificate to inactive.",
      "properties" : {
        "Action" : {
          "type" : "string",
          "enum" : [ "DEACTIVATE", "UNSET_VALUE" ]
        }
      },
      "required" : [ "Action" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "ActionName" : {
      "description" : "A unique identifier for the mitigation action.",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9:_-]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "RoleArn" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ActionParams" : {
      "$ref" : "#/definitions/ActionParams"
    },
    "MitigationActionArn" : {
      "type" : "string"
    },
    "MitigationActionId" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ActionName" ],
  "required" : [ "RoleArn", "ActionParams" ],
  "createOnlyProperties" : [ "/properties/ActionName" ],
  "readOnlyProperties" : [ "/properties/MitigationActionArn", "/properties/MitigationActionId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iot:CreateMitigationAction", "iot:DescribeMitigationAction", "iot:TagResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "iot:DescribeMitigationAction", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iot:UpdateMitigationAction", "iot:ListTagsForResource", "iot:UntagResource", "iot:TagResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "iot:DescribeMitigationAction", "iot:DeleteMitigationAction" ]
    },
    "list" : {
      "permissions" : [ "iot:ListMitigationActions" ]
    }
  }
}
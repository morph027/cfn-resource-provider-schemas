SCHEMA = {
  "typeName" : "AWS::FIS::TargetAccountConfiguration",
  "description" : "Resource schema for AWS::FIS::TargetAccountConfiguration",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-fis.git",
  "definitions" : {
    "TargetExperimentTemplateId" : {
      "type" : "string",
      "description" : "The ID of the experiment template."
    },
    "TargetAccountId" : {
      "type" : "string",
      "description" : "The AWS account ID of the target account.",
      "maxLength" : 512
    },
    "TargetAccountRoleArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of an IAM role for the target account.",
      "maxLength" : 1224
    },
    "TargetAccountConfigurationDescription" : {
      "type" : "string",
      "description" : "The description of the target account.",
      "maxLength" : 512
    }
  },
  "properties" : {
    "ExperimentTemplateId" : {
      "$ref" : "#/definitions/TargetExperimentTemplateId"
    },
    "AccountId" : {
      "$ref" : "#/definitions/TargetAccountId"
    },
    "RoleArn" : {
      "$ref" : "#/definitions/TargetAccountRoleArn"
    },
    "Description" : {
      "$ref" : "#/definitions/TargetAccountConfigurationDescription"
    }
  },
  "additionalProperties" : False,
  "required" : [ "ExperimentTemplateId", "AccountId", "RoleArn" ],
  "createOnlyProperties" : [ "/properties/ExperimentTemplateId", "/properties/AccountId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "primaryIdentifier" : [ "/properties/ExperimentTemplateId", "/properties/AccountId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "fis:CreateTargetAccountConfiguration" ]
    },
    "read" : {
      "permissions" : [ "fis:GetTargetAccountConfiguration" ]
    },
    "update" : {
      "permissions" : [ "fis:UpdateTargetAccountConfiguration" ]
    },
    "delete" : {
      "permissions" : [ "fis:DeleteTargetAccountConfiguration" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ExperimentTemplateId" : {
            "$ref" : "resource-schema.json#/properties/ExperimentTemplateId"
          }
        },
        "required" : [ "ExperimentTemplateId" ]
      },
      "permissions" : [ "fis:ListTargetAccountConfigurations" ]
    }
  }
}
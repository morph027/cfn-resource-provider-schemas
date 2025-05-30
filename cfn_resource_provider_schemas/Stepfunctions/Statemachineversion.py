SCHEMA = {
  "typeName" : "AWS::StepFunctions::StateMachineVersion",
  "description" : "Resource schema for StateMachineVersion",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-stepfunctions.git",
  "definitions" : { },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "StateMachineArn" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "StateMachineRevisionId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "Description" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048
    }
  },
  "required" : [ "StateMachineArn" ],
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/StateMachineArn", "/properties/StateMachineRevisionId", "/properties/Description" ],
  "writeOnlyProperties" : [ "/properties/StateMachineArn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "states:PublishStateMachineVersion", "states:ListStateMachineVersions", "states:DescribeStateMachine" ]
    },
    "read" : {
      "permissions" : [ "states:DescribeStateMachine" ]
    },
    "delete" : {
      "permissions" : [ "states:DeleteStateMachineVersion", "states:DescribeStateMachine" ]
    },
    "list" : {
      "permissions" : [ "states:ListStateMachineVersions" ],
      "handlerSchema" : {
        "properties" : {
          "StateMachineArn" : {
            "$ref" : "resource-schema.json#/properties/StateMachineArn"
          }
        },
        "required" : [ "StateMachineArn" ]
      }
    }
  }
}
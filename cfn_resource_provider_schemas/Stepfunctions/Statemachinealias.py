SCHEMA = {
  "typeName" : "AWS::StepFunctions::StateMachineAlias",
  "description" : "Resource schema for StateMachineAlias",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-stepfunctions.git",
  "definitions" : {
    "RoutingConfigurationVersion" : {
      "type" : "object",
      "properties" : {
        "StateMachineVersionArn" : {
          "type" : "string",
          "description" : "The Amazon Resource Name (ARN) that identifies one or two state machine versions defined in the routing configuration.",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "Weight" : {
          "type" : "integer",
          "description" : "The percentage of traffic you want to route to the state machine version. The sum of the weights in the routing configuration must be equal to 100.",
          "minimum" : 0,
          "maximum" : 100
        }
      },
      "required" : [ "StateMachineVersionArn", "Weight" ],
      "additionalProperties" : False
    },
    "RoutingConfiguration" : {
      "type" : "array",
      "description" : "The routing configuration of the alias. One or two versions can be mapped to an alias to split StartExecution requests of the same state machine.",
      "minItems" : 1,
      "maxItems" : 2,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/RoutingConfigurationVersion"
      }
    },
    "DeploymentPreference" : {
      "type" : "object",
      "description" : "The settings to enable gradual state machine deployments.",
      "properties" : {
        "StateMachineVersionArn" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "Type" : {
          "type" : "string",
          "description" : "The type of deployment to perform.",
          "enum" : [ "LINEAR", "ALL_AT_ONCE", "CANARY" ]
        },
        "Percentage" : {
          "type" : "integer",
          "description" : "The percentage of traffic to shift to the new version in each increment.",
          "minimum" : 1,
          "maximum" : 99
        },
        "Interval" : {
          "type" : "integer",
          "description" : "The time in minutes between each traffic shifting increment.",
          "minimum" : 1,
          "maximum" : 2100
        },
        "Alarms" : {
          "type" : "array",
          "description" : "A list of CloudWatch alarm names that will be monitored during the deployment. The deployment will fail and rollback if any alarms go into ALARM state.",
          "minItems" : 1,
          "maxItems" : 100,
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 256
          }
        }
      },
      "required" : [ "StateMachineVersionArn", "Type" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048,
      "description" : "The ARN of the alias."
    },
    "Name" : {
      "type" : "string",
      "description" : "The alias name.",
      "minLength" : 1,
      "maxLength" : 80
    },
    "Description" : {
      "type" : "string",
      "description" : "An optional description of the alias.",
      "minLength" : 1,
      "maxLength" : 256
    },
    "RoutingConfiguration" : {
      "$ref" : "#/definitions/RoutingConfiguration"
    },
    "DeploymentPreference" : {
      "$ref" : "#/definitions/DeploymentPreference"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "oneOf" : [ {
    "required" : [ "RoutingConfiguration" ]
  }, {
    "required" : [ "DeploymentPreference" ]
  } ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "writeOnlyProperties" : [ "/properties/DeploymentPreference" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "states:CreateStateMachineAlias", "states:DescribeStateMachineAlias" ]
    },
    "read" : {
      "permissions" : [ "states:DescribeStateMachineAlias" ]
    },
    "update" : {
      "permissions" : [ "cloudwatch:DescribeAlarms", "states:UpdateStateMachineAlias", "states:DescribeStateMachineAlias" ],
      "timeoutInMinutes" : 2160
    },
    "delete" : {
      "permissions" : [ "states:DescribeStateMachineAlias", "states:DeleteStateMachineAlias" ]
    },
    "list" : {
      "permissions" : [ "states:ListStateMachineAliases" ],
      "handlerSchema" : {
        "properties" : {
          "RoutingConfiguration" : {
            "$ref" : "resource-schema.json#/properties/RoutingConfiguration"
          }
        },
        "required" : [ "RoutingConfiguration" ]
      }
    }
  }
}
SCHEMA = {
  "typeName" : "AWS::LookoutMetrics::Alert",
  "description" : "Resource Type definition for AWS::LookoutMetrics::Alert",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lookout-for-metrics.git",
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:([a-z\\d-]+):.*:.*:.*:.+"
    },
    "Action" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SNSConfiguration" : {
          "$ref" : "#/definitions/SNSConfiguration"
        },
        "LambdaConfiguration" : {
          "$ref" : "#/definitions/LambdaConfiguration"
        }
      }
    },
    "SNSConfiguration" : {
      "description" : "Configuration options for an SNS alert action.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "description" : "ARN of an IAM role that LookoutMetrics should assume to access the SNS topic.",
          "$ref" : "#/definitions/Arn"
        },
        "SnsTopicArn" : {
          "description" : "ARN of an SNS topic to send alert notifications to.",
          "$ref" : "#/definitions/Arn"
        }
      },
      "required" : [ "RoleArn", "SnsTopicArn" ]
    },
    "LambdaConfiguration" : {
      "description" : "Configuration options for a Lambda alert action.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RoleArn" : {
          "description" : "ARN of an IAM role that LookoutMetrics should assume to access the Lambda function.",
          "$ref" : "#/definitions/Arn"
        },
        "LambdaArn" : {
          "description" : "ARN of a Lambda to send alert notifications to.",
          "$ref" : "#/definitions/Arn"
        }
      },
      "required" : [ "RoleArn", "LambdaArn" ]
    }
  },
  "properties" : {
    "AlertName" : {
      "description" : "The name of the alert. If not provided, a name is generated automatically.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*"
    },
    "Arn" : {
      "description" : "ARN assigned to the alert.",
      "$ref" : "#/definitions/Arn"
    },
    "AlertDescription" : {
      "description" : "A description for the alert.",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : ".*\\S.*"
    },
    "AnomalyDetectorArn" : {
      "description" : "The Amazon resource name (ARN) of the Anomaly Detector to alert.",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:([a-z\\d-]+):.*:.*:.*:.+"
    },
    "AlertSensitivityThreshold" : {
      "description" : "A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.",
      "type" : "integer",
      "minimum" : 0,
      "maximum" : 100
    },
    "Action" : {
      "description" : "The action to be taken by the alert when an anomaly is detected.",
      "$ref" : "#/definitions/Action"
    }
  },
  "additionalProperties" : False,
  "required" : [ "AnomalyDetectorArn", "AlertSensitivityThreshold", "Action" ],
  "createOnlyProperties" : [ "/properties/AlertName", "/properties/AlertDescription", "/properties/AnomalyDetectorArn", "/properties/AlertSensitivityThreshold", "/properties/Action" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lookoutmetrics:CreateAlert", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "lookoutmetrics:DescribeAlert" ]
    },
    "delete" : {
      "permissions" : [ "lookoutmetrics:DeleteAlert" ]
    },
    "list" : {
      "permissions" : [ "lookoutmetrics:ListAlerts" ]
    }
  }
}
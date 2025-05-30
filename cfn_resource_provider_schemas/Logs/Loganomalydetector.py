SCHEMA = {
  "typeName" : "AWS::Logs::LogAnomalyDetector",
  "description" : "The AWS::Logs::LogAnomalyDetector resource specifies a CloudWatch Logs LogAnomalyDetector.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git",
  "tagging" : {
    "taggable" : False
  },
  "properties" : {
    "AccountId" : {
      "description" : "Account ID for owner of detector",
      "type" : "string"
    },
    "KmsKeyId" : {
      "description" : "The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.",
      "type" : "string",
      "maxLength" : 256
    },
    "DetectorName" : {
      "description" : "Name of detector",
      "type" : "string"
    },
    "LogGroupArnList" : {
      "description" : "List of Arns for the given log group",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "minLength" : 20,
        "maxLength" : 2048
      }
    },
    "EvaluationFrequency" : {
      "description" : "How often log group is evaluated",
      "type" : "string",
      "enum" : [ "FIVE_MIN", "TEN_MIN", "FIFTEEN_MIN", "THIRTY_MIN", "ONE_HOUR" ]
    },
    "FilterPattern" : {
      "description" : "",
      "type" : "string",
      "pattern" : ""
    },
    "AnomalyDetectorStatus" : {
      "description" : "Current status of detector.",
      "type" : "string"
    },
    "AnomalyVisibilityTime" : {
      "description" : "",
      "type" : "number"
    },
    "CreationTimeStamp" : {
      "description" : "When detector was created.",
      "type" : "number"
    },
    "LastModifiedTimeStamp" : {
      "description" : "When detector was lsat modified.",
      "type" : "number"
    },
    "AnomalyDetectorArn" : {
      "description" : "ARN of LogAnomalyDetector",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/AnomalyDetectorArn", "/properties/CreationTimeStamp", "/properties/LastModifiedTimeStamp", "/properties/AnomalyDetectorStatus" ],
  "writeOnlyProperties" : [ "/properties/AccountId" ],
  "primaryIdentifier" : [ "/properties/AnomalyDetectorArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "logs:CreateLogAnomalyDetector" ]
    },
    "read" : {
      "permissions" : [ "logs:GetLogAnomalyDetector" ]
    },
    "update" : {
      "permissions" : [ "logs:UpdateLogAnomalyDetector" ]
    },
    "delete" : {
      "permissions" : [ "logs:DeleteLogAnomalyDetector" ]
    },
    "list" : {
      "permissions" : [ "logs:ListLogAnomalyDetectors" ]
    }
  }
}
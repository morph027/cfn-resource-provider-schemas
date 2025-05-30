SCHEMA = {
  "typeName" : "AWS::RoboMaker::RobotApplicationVersion",
  "description" : "AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[\\w+=/,.@-]+:[\\w+=/,.@-]+:[\\w+=/,.@-]*:[0-9]*:[\\w+=,.@-]+(/[\\w+=,.@-]+)*"
    }
  },
  "properties" : {
    "Application" : {
      "$ref" : "#/definitions/Arn"
    },
    "CurrentRevisionId" : {
      "description" : "The revision ID of robot application.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 40,
      "pattern" : "[a-zA-Z0-9_.\\-]*"
    },
    "ApplicationVersion" : {
      "type" : "string"
    },
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Application" ],
  "readOnlyProperties" : [ "/properties/ApplicationVersion", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Application", "/properties/CurrentRevisionId" ],
  "taggable" : False,
  "handlers" : {
    "create" : {
      "permissions" : [ "robomaker:CreateRobotApplicationVersion", "s3:GetObject", "ecr:BatchGetImage", "ecr:GetAuthorizationToken", "ecr:BatchCheckLayerAvailability", "ecr-public:GetAuthorizationToken", "sts:GetServiceBearerToken" ]
    },
    "delete" : {
      "permissions" : [ "robomaker:DeleteRobotApplication", "robomaker:DescribeRobotApplication" ]
    },
    "read" : {
      "permissions" : [ "robomaker:DescribeRobotApplication" ]
    }
  }
}
SCHEMA = {
  "typeName" : "AWS::RoboMaker::RobotApplication",
  "description" : "This schema is for testing purpose only.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:[\\w+=/,.@-]+:[\\w+=/,.@-]+:[\\w+=/,.@-]*:[0-9]*:[\\w+=,.@-]+(/[\\w+=,.@-]+)*"
    },
    "Tags" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "^[a-zA-Z0-9-]{1,128}$" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 256
        }
      }
    },
    "SourceConfig" : {
      "type" : "object",
      "properties" : {
        "S3Bucket" : {
          "type" : "string",
          "description" : "The Arn of the S3Bucket that stores the robot application source."
        },
        "S3Key" : {
          "type" : "string",
          "description" : "The s3 key of robot application source."
        },
        "Architecture" : {
          "type" : "string",
          "description" : "The architecture of robot application.",
          "minLength" : 1,
          "maxLength" : 255,
          "enum" : [ "X86_64", "ARM64", "ARMHF" ]
        }
      },
      "required" : [ "S3Bucket", "S3Key", "Architecture" ],
      "additionalProperties" : False
    },
    "RobotSoftwareSuite" : {
      "description" : "The robot software suite used by the robot application.",
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "description" : "The name of robot software suite.",
          "enum" : [ "ROS", "ROS2", "General" ]
        },
        "Version" : {
          "type" : "string",
          "description" : "The version of robot software suite.",
          "enum" : [ "Kinetic", "Melodic", "Dashing" ]
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name of the robot application.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Sources" : {
      "description" : "The sources of the robot application.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/SourceConfig"
      }
    },
    "Environment" : {
      "description" : "The URI of the Docker image for the robot application.",
      "type" : "string"
    },
    "RobotSoftwareSuite" : {
      "$ref" : "#/definitions/RobotSoftwareSuite"
    },
    "CurrentRevisionId" : {
      "description" : "The revision ID of robot application.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 40
    },
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "additionalProperties" : False,
  "required" : [ "RobotSoftwareSuite" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "writeOnlyProperties" : [ "/properties/RobotSoftwareSuite/Version", "/properties/Sources" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "robomaker:CreateRobotApplication", "robomaker:TagResource", "robomaker:UntagResource", "ecr:BatchGetImage", "ecr:GetAuthorizationToken", "ecr:BatchCheckLayerAvailability", "ecr-public:GetAuthorizationToken", "sts:GetServiceBearerToken" ]
    },
    "read" : {
      "permissions" : [ "robomaker:DescribeRobotApplication" ]
    },
    "update" : {
      "permissions" : [ "robomaker:TagResource", "robomaker:UntagResource", "robomaker:UpdateRobotApplication", "ecr:BatchGetImage", "ecr:GetAuthorizationToken", "ecr:BatchCheckLayerAvailability", "ecr-public:GetAuthorizationToken" ]
    },
    "delete" : {
      "permissions" : [ "robomaker:DescribeRobotApplication", "robomaker:DeleteRobotApplication" ]
    },
    "list" : {
      "permissions" : [ "robomaker:ListRobotApplications" ]
    }
  }
}
SCHEMA = {
  "typeName" : "AWS::RoboMaker::Robot",
  "description" : "AWS::RoboMaker::Robot resource creates an AWS RoboMaker Robot.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-robomaker.git",
  "additionalProperties" : False,
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
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "Fleet" : {
      "description" : "The Amazon Resource Name (ARN) of the fleet.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1224
    },
    "Architecture" : {
      "description" : "The target architecture of the robot.",
      "type" : "string",
      "enum" : [ "X86_64", "ARM64", "ARMHF" ]
    },
    "GreengrassGroupId" : {
      "description" : "The Greengrass group id.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1224
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    },
    "Name" : {
      "description" : "The name for the robot.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    }
  },
  "required" : [ "GreengrassGroupId", "Architecture" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/GreengrassGroupId", "/properties/Name", "/properties/Architecture", "/properties/Fleet" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "robomaker:CreateRobot", "robomaker:RegisterRobot" ]
    },
    "read" : {
      "permissions" : [ "robomaker:DescribeRobot" ]
    },
    "delete" : {
      "permissions" : [ "robomaker:DescribeRobot", "robomaker:DeleteRobot", "robomaker:DeregisterRobot" ]
    },
    "list" : {
      "permissions" : [ "robomaker:ListRobots" ]
    },
    "update" : {
      "permissions" : [ "robomaker:TagResource", "robomaker:UntagResource" ]
    }
  }
}
SCHEMA = {
  "typeName" : "AWS::RoboMaker::Fleet",
  "description" : "AWS::RoboMaker::Fleet resource creates an AWS RoboMaker fleet. Fleets contain robots and can receive deployments.",
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
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    },
    "Name" : {
      "description" : "The name of the fleet.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "[a-zA-Z0-9_\\-]{1,255}$"
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "robomaker:CreateFleet" ]
    },
    "read" : {
      "permissions" : [ "robomaker:DescribeFleet" ]
    },
    "delete" : {
      "permissions" : [ "robomaker:DeleteFleet" ]
    },
    "update" : {
      "permissions" : [ "robomaker:TagResource", "robomaker:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "robomaker:ListFleets" ]
    }
  },
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Arn" ]
}
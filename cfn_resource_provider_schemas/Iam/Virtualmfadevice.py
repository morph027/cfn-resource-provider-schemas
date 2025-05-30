SCHEMA = {
  "typeName" : "AWS::IAM::VirtualMFADevice",
  "description" : "Resource Type definition for AWS::IAM::VirtualMFADevice",
  "additionalProperties" : False,
  "properties" : {
    "VirtualMfaDeviceName" : {
      "minLength" : 1,
      "maxLength" : 226,
      "pattern" : "[\\w+=,.@-]+",
      "type" : "string"
    },
    "Path" : {
      "minLength" : 1,
      "maxLength" : 512,
      "pattern" : "(\\u002F)|(\\u002F[\\u0021-\\u007F]+\\u002F)",
      "type" : "string"
    },
    "SerialNumber" : {
      "minLength" : 9,
      "maxLength" : 256,
      "pattern" : "[\\w+=/:,.@-]+",
      "type" : "string"
    },
    "Users" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "createOnlyProperties" : [ "/properties/VirtualMfaDeviceName", "/properties/Base32StringSeed", "/properties/Path" ],
  "readOnlyProperties" : [ "/properties/SerialNumber" ],
  "primaryIdentifier" : [ "/properties/SerialNumber" ],
  "required" : [ "Users" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateVirtualMFADevice", "iam:EnableMFADevice", "iam:ListVirtualMFADevices" ]
    },
    "read" : {
      "permissions" : [ "iam:ListVirtualMFADevices" ]
    },
    "update" : {
      "permissions" : [ "iam:TagMFADevice", "iam:UntagMFADevice" ]
    },
    "delete" : {
      "permissions" : [ "iam:DeleteVirtualMFADevice", "iam:DeactivateMFADevice" ]
    },
    "list" : {
      "permissions" : [ "iam:ListVirtualMFADevices" ]
    }
  }
}
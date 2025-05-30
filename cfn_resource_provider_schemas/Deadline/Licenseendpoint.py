SCHEMA = {
  "typeName" : "AWS::Deadline::LicenseEndpoint",
  "description" : "Definition of AWS::Deadline::LicenseEndpoint Resource Type",
  "definitions" : {
    "LicenseEndpointStatus" : {
      "type" : "string",
      "enum" : [ "CREATE_IN_PROGRESS", "DELETE_IN_PROGRESS", "READY", "NOT_READY" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DnsName" : {
      "type" : "string"
    },
    "LicenseEndpointId" : {
      "type" : "string",
      "pattern" : "^le-[0-9a-f]{32}$"
    },
    "SecurityGroupIds" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      },
      "maxItems" : 10,
      "minItems" : 1
    },
    "Status" : {
      "$ref" : "#/definitions/LicenseEndpointStatus"
    },
    "StatusMessage" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 0
    },
    "SubnetIds" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 32,
        "minLength" : 1
      },
      "maxItems" : 10,
      "minItems" : 1
    },
    "VpcId" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 1
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*):deadline:[a-z0-9-]+:[0-9]{12}:license-endpoint/le-[0-9a-z]{32}"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "insertionOrder" : False,
      "uniqueItems" : True
    }
  },
  "required" : [ "SecurityGroupIds", "SubnetIds", "VpcId" ],
  "readOnlyProperties" : [ "/properties/DnsName", "/properties/LicenseEndpointId", "/properties/Status", "/properties/StatusMessage", "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/SecurityGroupIds", "/properties/SubnetIds", "/properties/VpcId" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "deadline:TagResource", "deadline:UntagResource", "deadline:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateLicenseEndpoint", "deadline:GetLicenseEndpoint", "ec2:CreateTags", "ec2:CreateVpcEndpoint", "ec2:DescribeVpcEndpoints", "deadline:TagResource", "deadline:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetLicenseEndpoint", "deadline:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "deadline:TagResource", "deadline:UntagResource", "deadline:ListTagsForResource", "deadline:GetLicenseEndpoint" ]
    },
    "delete" : {
      "permissions" : [ "deadline:GetLicenseEndpoint", "deadline:DeleteLicenseEndpoint", "ec2:DeleteVpcEndpoints", "ec2:DescribeVpcEndpoints" ]
    },
    "list" : {
      "permissions" : [ "deadline:ListLicenseEndpoints" ]
    }
  },
  "additionalProperties" : False
}
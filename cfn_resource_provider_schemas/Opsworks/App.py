SCHEMA = {
  "typeName" : "AWS::OpsWorks::App",
  "description" : "Resource Type definition for AWS::OpsWorks::App",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "AppSource" : {
      "$ref" : "#/definitions/Source"
    },
    "Attributes" : {
      "type" : "object",
      "patternProperties" : {
        "[a-zA-Z0-9]+" : {
          "type" : "string"
        }
      }
    },
    "DataSources" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/DataSource"
      }
    },
    "Description" : {
      "type" : "string"
    },
    "Domains" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "EnableSsl" : {
      "type" : "boolean"
    },
    "Environment" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/EnvironmentVariable"
      }
    },
    "Name" : {
      "type" : "string"
    },
    "Shortname" : {
      "type" : "string"
    },
    "SslConfiguration" : {
      "$ref" : "#/definitions/SslConfiguration"
    },
    "StackId" : {
      "type" : "string"
    },
    "Type" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "Source" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Password" : {
          "type" : "string"
        },
        "Revision" : {
          "type" : "string"
        },
        "SshKey" : {
          "type" : "string"
        },
        "Type" : {
          "type" : "string"
        },
        "Url" : {
          "type" : "string"
        },
        "Username" : {
          "type" : "string"
        }
      }
    },
    "EnvironmentVariable" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Secure" : {
          "type" : "boolean"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "DataSource" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Arn" : {
          "type" : "string"
        },
        "DatabaseName" : {
          "type" : "string"
        },
        "Type" : {
          "type" : "string"
        }
      }
    },
    "SslConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Certificate" : {
          "type" : "string"
        },
        "Chain" : {
          "type" : "string"
        },
        "PrivateKey" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "Type", "Name", "StackId" ],
  "createOnlyProperties" : [ "/properties/Shortname", "/properties/StackId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}
SCHEMA = {
  "typeName" : "AWS::AppMesh::Mesh",
  "description" : "Resource Type definition for AWS::AppMesh::Mesh",
  "additionalProperties" : False,
  "properties" : {
    "Uid" : {
      "type" : "string"
    },
    "MeshName" : {
      "type" : "string"
    },
    "MeshOwner" : {
      "type" : "string"
    },
    "ResourceOwner" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Spec" : {
      "$ref" : "#/definitions/MeshSpec"
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
    "MeshSpec" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EgressFilter" : {
          "$ref" : "#/definitions/EgressFilter"
        },
        "ServiceDiscovery" : {
          "$ref" : "#/definitions/MeshServiceDiscovery"
        }
      }
    },
    "EgressFilter" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string"
        }
      },
      "required" : [ "Type" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "MeshServiceDiscovery" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IpPreference" : {
          "type" : "string"
        }
      }
    }
  },
  "createOnlyProperties" : [ "/properties/MeshName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/ResourceOwner", "/properties/MeshOwner", "/properties/Arn", "/properties/Uid" ]
}